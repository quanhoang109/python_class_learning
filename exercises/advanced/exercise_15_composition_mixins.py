"""
Exercise 15: Composition and Mixins

Build a Content Management System (CMS) using:
- Composition over inheritance
- Mixins for cross-cutting concerns
- Descriptors for validation

┌─────────────────────────────────────────────────────────────────────┐
│ CONCEPTS TO PRACTICE                                                │
├─────────────────────────────────────────────────────────────────────┤
│ 1. COMPOSITION     - Build complex objects from simpler components  │
│ 2. MIXINS          - Add reusable behavior to multiple classes      │
│ 3. DESCRIPTORS     - Custom attribute validation and access         │
│ 4. BEST PRACTICES  - "Has-a" vs "Is-a" relationships               │
└─────────────────────────────────────────────────────────────────────┘

Scenario: Build a CMS with different content types:
- Articles, Videos, Podcasts
- Each has: metadata, author, timestamps, tags
- Features: versioning, searchable, publishable, commentable

Instead of deep inheritance, use COMPOSITION and MIXINS!
"""

from abc import ABC, abstractmethod
from datetime import datetime
import json


# =============================================================================
# 1. DESCRIPTORS - Reusable Attribute Validation
# =============================================================================

class NonEmptyString:
    """Descriptor that ensures string is not empty."""

    def __init__(self, name, min_length=1, max_length=None):
        self.name = name
        self.min_length = min_length
        self.max_length = max_length

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, "")

    def __set__(self, instance, value):
        # TODO: Implement validation
        # - Must be a string
        # - Must be at least min_length
        # - Must be at most max_length (if set)
        pass


class PositiveInteger:
    """Descriptor that ensures value is a positive integer."""

    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, 0)

    def __set__(self, instance, value):
        # TODO: Implement validation
        # - Must be an integer
        # - Must be positive (> 0)
        pass


class EmailAddress:
    """Descriptor that validates email format."""

    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, "")

    def __set__(self, instance, value):
        # TODO: Implement validation
        # - Must be a string
        # - Must contain @ and .
        pass


# =============================================================================
# 2. COMPONENT CLASSES (for Composition)
# =============================================================================

class Author:
    """Author component - can be attached to any content."""

    # Use descriptors for validation
    name = NonEmptyString("name", min_length=2, max_length=100)
    email = EmailAddress("email")

    def __init__(self, name, email, bio=""):
        self.name = name
        self.email = email
        self.bio = bio

    def __str__(self):
        return f"{self.name} <{self.email}>"

    def to_dict(self):
        return {"name": self.name, "email": self.email, "bio": self.bio}


class Metadata:
    """Metadata component for SEO and categorization."""

    def __init__(self, title, description="", keywords=None):
        self.title = title
        self.description = description
        self.keywords = keywords or []

    def add_keyword(self, keyword):
        if keyword not in self.keywords:
            self.keywords.append(keyword)

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "keywords": self.keywords
        }


class MediaAttachment:
    """Media attachment component."""

    def __init__(self, url, media_type, alt_text=""):
        self.url = url
        self.media_type = media_type  # "image", "video", "audio"
        self.alt_text = alt_text

    def __str__(self):
        return f"[{self.media_type}] {self.url}"


class Comment:
    """Comment component."""

    def __init__(self, author_name, content, parent=None):
        self.author_name = author_name
        self.content = content
        self.parent = parent  # For threaded comments
        self.created_at = datetime.now()
        self.likes = 0

    def like(self):
        self.likes += 1

    def __str__(self):
        return f"{self.author_name}: {self.content[:50]}..."


class Version:
    """Version component for content versioning."""

    def __init__(self, version_number, content_snapshot, changed_by):
        self.version_number = version_number
        self.content_snapshot = content_snapshot
        self.changed_by = changed_by
        self.created_at = datetime.now()


# =============================================================================
# 3. MIXINS - Reusable Behavior
# =============================================================================

class TimestampMixin:
    """Adds timestamp tracking to any class."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def touch(self):
        """Update the modified timestamp."""
        self.updated_at = datetime.now()

    def get_age_days(self):
        """Get age in days since creation."""
        return (datetime.now() - self.created_at).days


class PublishableMixin:
    """Adds publishing functionality."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_published = False
        self.published_at = None
        self.is_draft = True

    def publish(self):
        """Publish the content."""
        # TODO: Implement
        # - Set is_published to True
        # - Set published_at to now
        # - Set is_draft to False
        pass

    def unpublish(self):
        """Unpublish the content."""
        # TODO: Implement
        pass

    def is_live(self):
        """Check if content is currently published."""
        return self.is_published and not self.is_draft


class TaggableMixin:
    """Adds tagging functionality."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tags = []

    def add_tag(self, tag):
        """Add a tag."""
        # TODO: Implement - avoid duplicates, lowercase
        pass

    def remove_tag(self, tag):
        """Remove a tag."""
        # TODO: Implement
        pass

    def has_tag(self, tag):
        """Check if has tag."""
        return tag.lower() in self.tags


class CommentableMixin:
    """Adds commenting functionality."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.comments = []
        self.comments_enabled = True

    def add_comment(self, author_name, content, parent=None):
        """Add a comment."""
        # TODO: Implement
        # - Check if comments are enabled
        # - Create Comment object
        # - Append to comments list
        pass

    def get_comments_count(self):
        """Get total comments count."""
        return len(self.comments)

    def disable_comments(self):
        self.comments_enabled = False

    def enable_comments(self):
        self.comments_enabled = True


class VersionableMixin:
    """Adds version history functionality."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.versions = []
        self.current_version = 1

    def save_version(self, content_snapshot, changed_by):
        """Save a new version."""
        # TODO: Implement
        # - Create Version object
        # - Increment current_version
        # - Add to versions list
        pass

    def get_version(self, version_number):
        """Get a specific version."""
        for v in self.versions:
            if v.version_number == version_number:
                return v
        return None

    def rollback(self, version_number):
        """Rollback to a specific version."""
        # TODO: Implement
        pass


class SearchableMixin:
    """Adds search functionality."""

    def get_searchable_text(self):
        """Override this to return searchable text."""
        return ""

    def matches_search(self, query):
        """Check if content matches search query."""
        query = query.lower()
        searchable = self.get_searchable_text().lower()
        return query in searchable


class SerializableMixin:
    """Adds JSON serialization."""

    def to_dict(self):
        """Convert to dictionary. Override for custom serialization."""
        result = {}
        for key, value in self.__dict__.items():
            if not key.startswith('_'):
                if hasattr(value, 'to_dict'):
                    result[key] = value.to_dict()
                elif isinstance(value, datetime):
                    result[key] = value.isoformat()
                elif isinstance(value, list):
                    result[key] = [
                        item.to_dict() if hasattr(item, 'to_dict') else str(item)
                        for item in value
                    ]
                else:
                    result[key] = value
        return result

    def to_json(self):
        """Convert to JSON string."""
        return json.dumps(self.to_dict(), indent=2, default=str)


# =============================================================================
# 4. CONTENT CLASSES (Using Composition + Mixins)
# =============================================================================

class Content(ABC):
    """Abstract base content class."""

    title = NonEmptyString("title", min_length=5, max_length=200)

    def __init__(self, title, author):
        self.title = title
        self.author = author  # Composition: has an Author
        self.metadata = None  # Composition: can have Metadata

    def set_metadata(self, title, description="", keywords=None):
        """Set metadata using composition."""
        self.metadata = Metadata(title, description, keywords)

    @abstractmethod
    def get_content_type(self):
        """Return the content type."""
        pass


class Article(
    TimestampMixin,
    PublishableMixin,
    TaggableMixin,
    CommentableMixin,
    VersionableMixin,
    SearchableMixin,
    SerializableMixin,
    Content
):
    """
    Article content type.
    Uses composition for author, metadata.
    Uses mixins for timestamps, publishing, tags, comments, versions, search.
    """

    def __init__(self, title, author, body=""):
        super().__init__(title, author)
        self.body = body
        self.featured_image = None  # Composition: can have MediaAttachment

    def get_content_type(self):
        return "article"

    def set_featured_image(self, url, alt_text=""):
        """Set featured image using composition."""
        self.featured_image = MediaAttachment(url, "image", alt_text)

    def get_searchable_text(self):
        """Return text for search indexing."""
        parts = [self.title, self.body]
        if self.metadata:
            parts.extend([self.metadata.title, self.metadata.description])
            parts.extend(self.metadata.keywords)
        return " ".join(parts)

    def get_word_count(self):
        """Get word count of body."""
        return len(self.body.split())

    def get_reading_time(self, words_per_minute=200):
        """Estimate reading time in minutes."""
        return max(1, self.get_word_count() // words_per_minute)


class Video(
    TimestampMixin,
    PublishableMixin,
    TaggableMixin,
    CommentableMixin,
    SearchableMixin,
    SerializableMixin,
    Content
):
    """
    Video content type.
    """

    duration = PositiveInteger("duration")

    def __init__(self, title, author, video_url, duration_seconds):
        super().__init__(title, author)
        self.video_url = video_url
        self.duration = duration_seconds  # Uses descriptor
        self.transcript = ""
        self.thumbnail = None

    def get_content_type(self):
        return "video"

    def set_thumbnail(self, url, alt_text=""):
        self.thumbnail = MediaAttachment(url, "image", alt_text)

    def get_searchable_text(self):
        parts = [self.title, self.transcript]
        if self.metadata:
            parts.extend([self.metadata.title, self.metadata.description])
        return " ".join(parts)

    def get_duration_formatted(self):
        """Get duration as HH:MM:SS."""
        hours = self.duration // 3600
        minutes = (self.duration % 3600) // 60
        seconds = self.duration % 60
        if hours > 0:
            return f"{hours}:{minutes:02d}:{seconds:02d}"
        return f"{minutes}:{seconds:02d}"


class Podcast(
    TimestampMixin,
    PublishableMixin,
    TaggableMixin,
    CommentableMixin,
    SearchableMixin,
    SerializableMixin,
    Content
):
    """
    Podcast episode content type.
    """

    def __init__(self, title, author, audio_url, duration_seconds, episode_number):
        super().__init__(title, author)
        self.audio_url = audio_url
        self.duration = duration_seconds
        self.episode_number = episode_number
        self.show_notes = ""
        self.guests = []  # Composition: list of Authors

    def get_content_type(self):
        return "podcast"

    def add_guest(self, name, email, bio=""):
        """Add a guest using composition."""
        guest = Author(name, email, bio)
        self.guests.append(guest)

    def get_searchable_text(self):
        parts = [self.title, self.show_notes]
        parts.extend([g.name for g in self.guests])
        if self.metadata:
            parts.extend([self.metadata.title, self.metadata.description])
        return " ".join(parts)


# =============================================================================
# 5. CMS CLASS (Coordinator)
# =============================================================================

class CMS:
    """Content Management System."""

    def __init__(self, name):
        self.name = name
        self.content = []
        self.authors = []

    def add_author(self, name, email, bio=""):
        """Add an author."""
        author = Author(name, email, bio)
        self.authors.append(author)
        return author

    def create_article(self, title, author, body=""):
        """Create a new article."""
        article = Article(title, author, body)
        self.content.append(article)
        return article

    def create_video(self, title, author, video_url, duration):
        """Create a new video."""
        video = Video(title, author, video_url, duration)
        self.content.append(video)
        return video

    def create_podcast(self, title, author, audio_url, duration, episode_num):
        """Create a new podcast."""
        podcast = Podcast(title, author, audio_url, duration, episode_num)
        self.content.append(podcast)
        return podcast

    def get_published(self):
        """Get all published content."""
        return [c for c in self.content if hasattr(c, 'is_live') and c.is_live()]

    def get_drafts(self):
        """Get all drafts."""
        return [c for c in self.content if hasattr(c, 'is_draft') and c.is_draft]

    def search(self, query):
        """Search all content."""
        return [c for c in self.content if c.matches_search(query)]

    def get_by_tag(self, tag):
        """Get content by tag."""
        return [c for c in self.content if hasattr(c, 'has_tag') and c.has_tag(tag)]

    def get_by_type(self, content_type):
        """Get content by type."""
        return [c for c in self.content if c.get_content_type() == content_type]


# =============================================================================
# TESTS
# =============================================================================

def run_tests():
    print("=" * 60)
    print("COMPOSITION AND MIXINS - CMS TESTS")
    print("=" * 60)

    # TODO: Uncomment tests after implementing

    # # Test 1: Descriptors
    # print("\n--- Test 1: Descriptors ---")
    # try:
    #     author = Author("", "invalid")  # Should fail - empty name
    # except ValueError as e:
    #     print(f"Caught validation error: {e}")
    #
    # author = Author("John Doe", "john@example.com", "A writer")
    # print(f"Valid author: {author}")

    # # Test 2: Composition
    # print("\n--- Test 2: Composition ---")
    # cms = CMS("My Blog")
    # author = cms.add_author("Alice", "alice@blog.com", "Tech writer")
    #
    # article = cms.create_article(
    #     "Understanding Composition",
    #     author,
    #     "Composition is a design principle..."
    # )
    # article.set_metadata("Composition Guide", "Learn about composition", ["python", "oop"])
    # article.set_featured_image("https://example.com/image.jpg", "Composition diagram")
    #
    # print(f"Article: {article.title}")
    # print(f"Author: {article.author}")
    # print(f"Metadata: {article.metadata.to_dict()}")
    # print(f"Featured image: {article.featured_image}")

    # # Test 3: Mixins
    # print("\n--- Test 3: Mixins ---")
    #
    # # TimestampMixin
    # print(f"Created at: {article.created_at}")
    # article.touch()
    # print(f"Updated at: {article.updated_at}")
    #
    # # TaggableMixin
    # article.add_tag("Python")
    # article.add_tag("OOP")
    # article.add_tag("python")  # Should not duplicate
    # print(f"Tags: {article.tags}")
    # print(f"Has 'python' tag: {article.has_tag('python')}")
    #
    # # PublishableMixin
    # print(f"Is live: {article.is_live()}")
    # article.publish()
    # print(f"After publish - Is live: {article.is_live()}")
    # print(f"Published at: {article.published_at}")
    #
    # # CommentableMixin
    # article.add_comment("Bob", "Great article!")
    # article.add_comment("Carol", "Very helpful, thanks!")
    # print(f"Comments: {article.get_comments_count()}")

    # # Test 4: VersionableMixin
    # print("\n--- Test 4: Version History ---")
    # article.save_version(article.body, "Alice")
    # article.body = "Updated content..."
    # article.save_version(article.body, "Alice")
    # print(f"Current version: {article.current_version}")
    # print(f"Version history: {len(article.versions)} versions")

    # # Test 5: SearchableMixin
    # print("\n--- Test 5: Search ---")
    # print(f"Matches 'composition': {article.matches_search('composition')}")
    # print(f"Matches 'inheritance': {article.matches_search('inheritance')}")

    # # Test 6: SerializableMixin
    # print("\n--- Test 6: Serialization ---")
    # print("JSON output:")
    # print(article.to_json())

    # # Test 7: Different Content Types
    # print("\n--- Test 7: Different Content Types ---")
    # video = cms.create_video(
    #     "Python Tutorial",
    #     author,
    #     "https://youtube.com/...",
    #     3600  # 1 hour
    # )
    # video.add_tag("tutorial")
    # video.publish()
    # print(f"Video: {video.title} ({video.get_duration_formatted()})")
    #
    # podcast = cms.create_podcast(
    #     "Tech Talk Episode 1",
    #     author,
    #     "https://podcast.com/...",
    #     2400,  # 40 minutes
    #     1
    # )
    # podcast.add_guest("Bob Smith", "bob@guest.com", "Expert in Python")
    # podcast.publish()
    # print(f"Podcast: {podcast.title} with {len(podcast.guests)} guests")

    # # Test 8: CMS Operations
    # print("\n--- Test 8: CMS Operations ---")
    # print(f"Total content: {len(cms.content)}")
    # print(f"Published: {len(cms.get_published())}")
    # print(f"Articles: {len(cms.get_by_type('article'))}")
    # print(f"Content with 'python' tag: {len(cms.get_by_tag('python'))}")
    # print(f"Search 'tutorial': {len(cms.search('tutorial'))} results")

    print("\n" + "=" * 60)
    print("Implement the mixins and uncomment tests!")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()
